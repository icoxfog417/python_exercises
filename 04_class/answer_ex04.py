# -*- coding: utf-8 -*-
import unittest


class Bot():

    def __init__(self, owner_name):
        self.owner_name = name

    def reply(self, call):
        if self.owner_name in call:
            return "Hello my Boss!"
        else:
            return "Hello"


class TestBot(unittest.TestCase):

    def test_bot_reply(self):
        bot = Bot("Angy")
        self.assertEqual("Hello", bot.reply("Hi, I'm Bill.'"))
        self.assertEqual("Hello my Boss!", bot.reply("Hi, I'm Angy."))


if __name__ == "__main__":
    unittest.main()
