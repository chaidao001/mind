from datetime import datetime
from unittest import TestCase

from src.utils.configs import Configs
from src.utils.sessionmanager import SessionManager


class TestSessionManager(TestCase):
    def setUp(self):
        self.session_manager = SessionManager(Configs())

    def test_is_expired_expired_returnTrue(self):
        self._set_up_expired_session()

        is_expired = self.session_manager._is_expired()

        self.assertEqual(is_expired, True)

    def test_is_expired_notExpired_returnFalse(self):
        self._set_up_non_expired_session()

        is_expired = self.session_manager._is_expired()

        self.assertEqual(is_expired, False)

    def test_is_expired_noneRequestedTime_returnTrue(self):
        self.session_manager._requested_time = None

        is_expired = self.session_manager._is_expired()

        self.assertEqual(is_expired, True)

    def test_get_session_expired_getNewSession(self):
        current_session = "current_session"
        self._set_up_expired_session()
        self.session_manager._session = current_session

        new_session = self.session_manager.get_session()

        self.assertTrue(new_session != current_session)
        self.assertTrue(self.session_manager._session != current_session)

    def test_get_session_noneRequestedTime_getNewSession(self):
        current_session = "current_session"
        self.session_manager._requested_time = None
        self.session_manager._session = current_session

        new_session = self.session_manager.get_session()

        self.assertTrue(new_session != current_session)
        self.assertTrue(self.session_manager._session != current_session)

    def test_get_session_notExpired_getCurrentSession(self):
        current_session = "current_session"
        self._set_up_non_expired_session()
        self.session_manager._session = current_session

        new_session = self.session_manager.get_session()

        self.assertEqual(new_session, current_session)
        self.assertEqual(self.session_manager._session, current_session)

    def _set_up_expired_session(self):
        self.session_manager._session_duration_hour = -1
        self.session_manager._requested_time = datetime.now()

    def _set_up_non_expired_session(self):
        self.session_manager._session_duration_hour = 1
        self.session_manager._requested_time = datetime.now()
