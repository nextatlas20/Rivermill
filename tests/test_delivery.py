from rivermill.api.signature import compute_signature, verify_signature


def test_signature_round_trip():
    body = b'{"event": "created"}'
    header = compute_signature("s3cret", body)
    assert verify_signature("s3cret", body, header)


def test_signature_rejects_tampering():
    header = compute_signature("s3cret", b"original")
    assert not verify_signature("s3cret", b"tampered", header)
