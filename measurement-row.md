# Measurement Row

| Baseline | Candidate | Path | Method | Result | Limit |
|---|---|---|---|---|---|
| X25519 | X25519MLKEM768 | Client key share + server key share | Specification-derived encoded key shares (RFC 10024) | +2,272 bytes | Key-share delta only. Excludes TLS framing, certificates, CertificateVerify, tickets, records, and retransmissions. |
| P-256 | X25519MLKEM768 | Client key share + server key share | Specification-derived encoded key shares (RFC 10024) | +2,206 bytes | Key-share delta only. Excludes TLS framing, certificates, CertificateVerify, tickets, records, and retransmissions. |
