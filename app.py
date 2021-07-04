import json
import logging
import mt940
import falcon
import base64

class MT940Parser:

	def parseToJson(self, data):

		transactions = mt940.models.Transactions(processors=dict(
		    pre_statement=[
		        mt940.processors.add_currency_pre_processor('IDR'),
		    ],
		))

		transactions.parse(data)
		return json.dumps(transactions, cls=mt940.JSONEncoder)

class MT940Error(Exception):

    @staticmethod
    def handle(ex, req, resp, params):
        # TODO: Log the error, clean up, etc. before raising
        raise falcon.HTTPInternalServerError()


def max_body(limit):

    def hook(req, resp, resource, params):
        length = req.content_length
        if length is not None and length > limit:
            msg = ('The size of the request is too large. The body must not '
                   'exceed ' + str(limit) + ' bytes in length.')

            raise falcon.HTTPPayloadTooLarge(
                title='Request body is too large', description=msg)

    return hook

class JSONTranslator:

    def process_request(self, req, resp):
        if req.content_length in (None, 0):
            # Nothing to do
            return

        body = req.stream.read()
        if not body:
            raise falcon.HTTPBadRequest(title='Empty request body',
                                        description='A valid JSON document is required.')

        try:
            req.context.doc = json.loads(body.decode('utf-8'))

        except (ValueError, UnicodeDecodeError):
            description = ('Could not decode the request body. The '
                           'JSON was incorrect or not encoded as '
                           'UTF-8.')

            raise falcon.HTTPBadRequest(title='Malformed JSON',
                                        description=description)

class MT940Resource:

    def __init__(self, parser):
        self.parser = parser
        self.logger = logging.getLogger('mt940parser.' + __name__)

    @falcon.before(max_body(100 * 1024 * 1024))
    def on_post(self, req, resp):
        try:
            payload = req.context.doc
        except AttributeError:
            raise falcon.HTTPBadRequest(
                title='Missing text to parse',
                description='Please specify text in the request body.')

        encoded = base64.b64decode(payload["text"])
        result = self.parser.parseToJson(encoded.decode("utf-8"))

        resp.status = falcon.HTTP_200
        resp.text = result


# Configure your WSGI server to load "things.app" (app is a WSGI callable)
app = falcon.App(middleware=[JSONTranslator()])

parser = MT940Parser()
mt = MT940Resource(parser)

app.add_route('/parse', mt)
app.add_error_handler(MT940Error, MT940Error.handle)