# Py Swift

Simple API to parse MT 940 text

## How to run

```bash
docker run -d -p 8000:8000 py-swift
```

## Usage

- Encode your MT940 file using base64 encoding
- Pass value  in `text` field in JSON payload

```bash
curl --location --request POST 'localhost:8000/parse' \
--header 'Content-Type: application/json' \
--data '{"text": "ezE6RjAxQkFOSyBNQU5ESVJJfXsyOkk5NDJDVVNUT01FUiBOQU1FfXs0Ogo6MjA6QUNDT1VOVCBOQU1FCjoyNTpJRDAwMDA4MTI0MDEwMDAxMjQwMDA0MDM5OTk5CjoyOEM6MDAwMDEvMDAxCjozNEY6SURSMCwKOjEzRDoxMDA4MDIxMDAwKzA3MDAKOjYxOjEwMDgwMjA4MDJENTAwMDAwMCwwME5UUkYwMDAwMDAwMC8vMTAxNTAwNDYyMDIwMDAzMjcwMTEKOjg2OlZlbmRvciBQYXltZW50IDEyMzQ1Njc4OTAxMjM0NTY3ODkKOjYxOjEwMDgwMjA4MDJENTAwMCwwME5DSEcxMDc2Mzc5NS8vMTAxNTUwNDU4MDAwMDA2NDEzMDQKOjg2OlRyYW5zZmVyIEZlZSAxMjM0NTY3ODkwMTIzNDU2Nzg5Cjo2MToxMDA4MDIwODAyRDEwMDAwMDAsMDBOVFJGMTA3NjM4MTAvLzEwMTU1MDQ1ODAwMDAwNjUxMzE0Cjo4NjpJTlYuIDAwNC9JTlYtQU5UVi9JVi8xMCAvIEFOVFYKOjYxOjEwMDgwMjA4MDJDNDAwMDAsMDBOVFJGMTA3NjM4MTEvLzEwMTU1MDQ1ODAwMDAwNjYxMzA0Cjo4NjpEQVJJIFBUIFNVQVJBIE1BS01VUgo6OTBEOjNJRFI2MDA1MDAwLDAwCjo5MEM6MUlEUjQwMDAwLDAwCi19"}'
```

will give you

```json
{
  "transaction_reference": "ACCOUNT NAME",
  "account_identification": "ID00008124010001240004039999",
  "statement_number": "00001",
  "sequence_number": "001",
  "d_floor_limit": {
    "amount": "0",
    "currency": "IDR"
  },
  "c_floor_limit": {
    "amount": "0",
    "currency": "IDR"
  },
  "date": "2010-08-02 10:00:00+11:40",
  "sum_debit_entries": {
    "amount": "-6005000.00",
    "currency": "IDR",
    "number": "3"
  },
  "sum_credit_entries": {
    "amount": "40000.00",
    "currency": "IDR",
    "number": "1"
  },
  "transactions": [
    {
      "status": "D",
      "funds_code": null,
      "amount": {
        "amount": "-5000000.00",
        "currency": "IDR"
      },
      "id": "NTRF",
      "customer_reference": "00000000//101500",
      "bank_reference": null,
      "extra_details": "46202000327011",
      "currency": "IDR",
      "date": "2010-08-02",
      "entry_date": "2010-08-02",
      "guessed_entry_date": "2010-08-02",
      "transaction_details": "Vendor Payment 1234567890123456789"
    },
    {
      "status": "D",
      "funds_code": null,
      "amount": {
        "amount": "-5000.00",
        "currency": "IDR"
      },
      "id": "NCHG",
      "customer_reference": "10763795//101550",
      "bank_reference": null,
      "extra_details": "45800000641304",
      "currency": "IDR",
      "date": "2010-08-02",
      "entry_date": "2010-08-02",
      "guessed_entry_date": "2010-08-02",
      "transaction_details": "Transfer Fee 1234567890123456789"
    },
    {
      "status": "D",
      "funds_code": null,
      "amount": {
        "amount": "-1000000.00",
        "currency": "IDR"
      },
      "id": "NTRF",
      "customer_reference": "10763810//101550",
      "bank_reference": null,
      "extra_details": "45800000651314",
      "currency": "IDR",
      "date": "2010-08-02",
      "entry_date": "2010-08-02",
      "guessed_entry_date": "2010-08-02",
      "transaction_details": "INV. 004/INV-ANTV/IV/10 / ANTV"
    },
    {
      "status": "C",
      "funds_code": null,
      "amount": {
        "amount": "40000.00",
        "currency": "IDR"
      },
      "id": "NTRF",
      "customer_reference": "10763811//101550",
      "bank_reference": null,
      "extra_details": "45800000661304",
      "currency": "IDR",
      "date": "2010-08-02",
      "entry_date": "2010-08-02",
      "guessed_entry_date": "2010-08-02",
      "transaction_details": "DARI PT SUARA MAKMUR"
    }
  ]
}
```
