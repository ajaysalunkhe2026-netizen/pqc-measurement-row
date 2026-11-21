# Measuring the Key-Exchange Path

Selected group after Finished is the measurement. Handshake success is not. This lab compares the encoded TLS key shares for a classical baseline and the hybrid X25519MLKEM768 candidate, using specification-derived sizes rather than observed network traffic.

**Numbers below are specification-derived from RFC 10024, not packet captures.**

> Lab view. The label is not the measurement.

## Measurement

See [measurement-row.md](measurement-row.md) for the comparison and its limitations.

## Selected group check

Run the check from your terminal:

```bash
python selected_group_check.py X25519MLKEM768
```

Expected output:

```text
PASS: negotiated group is X25519MLKEM768
```

Test a classical fallback:

```bash
python selected_group_check.py X25519
```

Expected output:

```text
FAIL: expected X25519MLKEM768, got X25519
```

The script checks a supplied group name. It does not capture traffic or independently inspect a TLS handshake.

## Author

Ajay Salunkhe
