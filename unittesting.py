import pytest
from main import GymMembership

class TestGymMembership:

    def setup_method(self, method):  # pytest convention for setup
        self.membership = GymMembership()

    def test_select_membership_plan_valid(self):
        self.membership.select_membership_plan('Basic', 1)
        assert self.membership.selected_plan == 'Basic'
        assert self.membership.num_members == 1

    def test_select_membership_plan_invalid(self):
        with pytest.raises(ValueError):
            self.membership.select_membership_plan('Error', 1)

    def test_add_additional_features_valid(self):
        self.membership.select_membership_plan('Premium', 1)
        self.membership.add_additional_features(['Personal Training', 'Group Classes'])
        assert self.membership.selected_features == ['Personal Training', 'Group Classes']

    def test_add_additional_features_invalid(self):
        with pytest.raises(ValueError):
            self.membership.add_additional_features(['Invalid Feature'])

    def test_calculate_cost_basic_plan(self):
        self.membership.select_membership_plan('Basic', 1)
        assert self.membership.calculate_cost() == 50  # Use direct equality operator

if __name__ == '__main__':
    pytest.main()  # Use pytest.main() to run tests