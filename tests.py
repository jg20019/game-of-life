import unittest
import life as l

class TestGameOfLife(unittest.TestCase):
    def test_check_live(self):
        world = l.make_world()

        c1 = (1,2)
        c2 = (2,2)
        c3 = (3,2)

        c4 = (0,0)
        c5 = (5,5)
        c6 = (5,6)
        c7 = (1,4)

        self.assertEquals(l.check_live(c1,world),l.LIVE)
        self.assertEquals(l.check_live(c2,world),l.LIVE)
        self.assertEquals(l.check_live(c3,world),l.LIVE)

        self.assertEquals(l.check_live(c4,world),l.DEAD)
        self.assertEquals(l.check_live(c5,world),l.DEAD)
        self.assertEquals(l.check_live(c6,world),l.DEAD)
        self.assertEquals(l.check_live(c7,world),l.DEAD)


if __name__ == '__main__':
    unittest.main()
        

        
