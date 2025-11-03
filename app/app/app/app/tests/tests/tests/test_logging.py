import logging

def test_logging(caplog):
    caplog.set_level(logging.INFO)
    logging.info("Test message")
    assert "Test message" in caplog.text
