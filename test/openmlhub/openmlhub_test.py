""" Module tests
"""
import sys
from openmlhub import model_logger, OpenMLHubConf

def test_openmlhub_imported():
    assert "openmlhub" in sys.modules

def test_openmlhub_logger():
    conf = OpenMLHubConf("","", "")
    model_logger(conf)