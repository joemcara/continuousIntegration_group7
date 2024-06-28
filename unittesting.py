""" Unit Testing """
import unittest
from main import GymMembership

class TestGymMembership(unittest.TestCase):
    """ Testing """
    def setUp(self):
        # Configurar una instancia de GymMembership para cada prueba
        self.membership = GymMembership()

    def test_select_membership_plan_valid(self):
        """ Test select member Valid Select Plan """
        self.membership.select_membership_plan('Basic', 1)
        self.assertEqual(self.membership.selected_plan, 'Basic')
        self.assertEqual(self.membership.num_members, 1)

    def test_select_membership_plan_invalid(self):
        """ Test select member Invalid Select Plan"""
        with self.assertRaises(ValueError):
            self.membership.select_membership_plan('Error', 1)

    def test_add_additional_features_valid(self):
        """ Test add additional features Valid Feature"""
        self.membership.select_membership_plan('Premium', 1)
        self.membership.add_additional_features(['Personal Training', 'Group Classes'])
        self.assertEqual(self.membership.selected_features, ['Personal Training', 'Group Classes'])

    def test_add_additional_features_invalid(self):
        """ Test add additional features Invalid Feature """
        with self.assertRaises(ValueError):
            self.membership.add_additional_features(['Invalid Feature'])

    def test_calculate_cost_basic_plan(self):
        """ Test calculate cost basic plan valid"""
        self.membership.select_membership_plan('Basic', 1)
        self.assertEqual(self.membership.calculate_cost(), 50)

if __name__ == '__main__':
    unittest.main()
    