from unittest import TestCase
from lab18 import damerau_levenshtein_distance as dist

__author__ = 'vks'


class Test(TestCase):
    def test_empty1(self):
        s1 = ""
        s2 = ""
        self.assertEqual(dist(s1, s2), 0)

    def test_empty2(self):
        s1 = ""
        s2 = "abacaba"
        self.assertEqual(dist(s1, s2), 7)

    def test_empty3(self):
        s1 = "abacabadaba"
        s2 = ""
        self.assertEqual(dist(s1, s2), 11)

    def test_deletion1(self):
        s1 = "lorem ipsum"
        s2 = "lrem ipsum"
        self.assertEqual(dist(s1, s2), 1)

    def test_deletion2(self):
        s1 = "some vowels are missing!"
        s2 = "sm vwls r mssng!"
        self.assertEqual(dist(s1, s2), 8)

    def test_deletion3(self):
        s1 = "aaaaa"
        s2 = "aaa"
        self.assertEqual(dist(s1, s2), 2)

    def test_deletion4(self):
        # Hint: deletions are
        #   Danny -> Dann
        #   Resident -> Reside
        #   Well, you know, Alvin -> Well, Alvin
        #   Clairmont's -> Clairmont
        #   here -> hre
        #   Even if you -> Even you
        #   running -> run
        #   might still break -> might break
        #   Well, you're -> you're
        # 35 overall
        s1 = """Danny Riordan, Clermont Resident: Well, you know, Alvin, there's a lot of hills bigger than Clairmont's
                    between here and Zion. Even if you get that mower running again, it might still break down.
                Alvin Straight: Well, you're a kind man talking to a stubborn man."""
        s2 = """Dann Riordan, Clermont Reside: Well, Alvin, there's a lot of hills bigger than Clairmont
                    between hre and Zion. Even you get that mower run again, it might break down.
                Alvin Straight: you're a kind man talking to a stubborn man."""
        self.assertEqual(dist(s1, s2), 35)

    def test_insertion(self):
        s1 = "Wow, such string"
        s2 = "Wow, much python, such string"
        self.assertEqual(dist(s1, s2), 13)

    def test_insertion2(self):
        # Hint: insertions are
        #   Polonus -> Polonius
        #   read -> read,
        #   Words, words -> Words, words, words
        #   mater -> matter
        #   Hamlet -> Hamlet:
        #   lord -> lord.
        # 12 overall
        s1 = """Lord Polonus: What do you read my lord?
                Hamlet: Words, words.
                Lord Polonius: What is the mater, my lord?
                Hamlet Between who?
                Lord Polonius: I mean, the matter that you read, my lord"""
        s2 = """Lord Polonius: What do you read, my lord?
                Hamlet: Words, words, words.
                Lord Polonius: What is the matter, my lord?
                Hamlet: Between who?
                Lord Polonius: I mean, the matter that you read, my lord."""
        self.assertEqual(dist(s1, s2), 12)

    def test_replacement1(self):
        s1 = "There's a mistake samewhere here..."
        s2 = "There's a mistake somewhere here..."
        self.assertEqual(dist(s1, s2), 1)

    def test_replacement2(self):
        # Hint: replacements are
        #   drink -> blink
        #   deer -> dead
        #   fact -> fast
        #   car -> can
        #   neck -> back
        #   loot -> look
        #   Ant -> And
        #   hack -> Luck
        # 12 overall
        s1 = "Don't drink. Blink and you're deer. They are fact. Faster than you car believe. " \
             "Don't turn your neck. Don't loot away. Ant don't blink. Good hack."
        s2 = "Don't blink. Blink and you're dead. They are fast. Faster than you can believe. " \
             "Don't turn your back. Don't look away. And don't blink. Good Luck."
        self.assertEqual(dist(s1, s2), 12)

    def test_transpositions(self):
        s1 = "oLkos ilek osemhtnig si rwnog"
        s2 = "Looks like something is wrong"
        self.assertEqual(dist(s1, s2), 11)

    def test_transpositions2(self):
        # Hint: transpositions are
        #   sene -> seen
        #   thigns -> things
        #   eppole -> people
        #   woudln't -> wouldn't
        #   Atatck -> Attack
        #   fof -> off
        #   shoudler -> shoulder
        #   rOion -> Orion
        #   wacthed -> watched
        #   giltter -> glitter
        #   dakr -> dark
        #   teh -> the
        #   lAl -> All
        #   thsoe -> those
        #   momnets -> moments
        #   tmie -> time
        #   taers -> tears
        #   rani -> rain
        # 19 overall
        s1 = """I've sene thigns you eppole woudln't believe. Atatck ships on fire fof the shoudler of rOion.
                I wacthed C-beams giltter in the dakr near teh Tannhäuser Gate. lAl thsoe momnets will be lost in tmie,
                like taers...in...rani. Time to die."""
        s2 = """I've seen things you people wouldn't believe. Attack ships on fire off the shoulder of Orion.
                I watched C-beams glitter in the dark near the Tannhäuser Gate. All those moments will be lost in time,
                like tears...in...rain. Time to die."""
        self.assertEqual(dist(s1, s2), 19)

    def test_combined_tiny(self):
        s1 = "aba"
        s2 = "stables"
        self.assertEqual(dist(s1, s2), 5)

    def test_combined_small(self):
        s1 = "Levenshtien"
        s2 = "Frankenstein"
        self.assertEqual(dist(s1, s2), 7)

    def test_combined_medium(self):
        s1 = """LOG ENTRY: SOL 61 How come Aquaman can control whales? They’re mammals! Makes no sense."""
        s2 = """Maybe I’ll post a consumer review. “Brought product to surface of Mars. It stopped working. 0/10."""
        self.assertEqual(dist(s1, s2), 79)
