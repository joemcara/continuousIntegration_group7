""" Team 7 """
class GymMembership:
    """Gym Membership Management System"""

    def _init_(self):
        self.membership_plans = {
        'Basic': {'cost': 50, 
                  'benefits': ['Access to gym equipment'], 
                  'available': True},
        'Premium': {'cost': 100, 
                    'benefits': ['Access to gym equipment', 
                                 'Access to exclusive gym facilities', 
                                 'Specialized training programs'], 
                    'available': True},
        'Family': {'cost': 150, 
                   'benefits': ['Access to gym equipment', 
                                'Specialized training programs'], 
                                'available': False}
        }
        self.additional_features = {
            'Personal Training': 25,
            'Group Classes': 15
        }
        self.selected_plan = None
        self.selected_features = []
        self.num_members = 1
        self.total_cost = 0
        self.total_discount = 0

    def display_membership_plans(self):
        """Function display membership plans"""
        print("Available Membership Plans:")
        for plan, details in self.membership_plans.items():
            print(f"{plan}: ${details['cost']} - Benefits: {', '.join(details['benefits'])}")

    def display_additional_features(self):
        """Function display additional features"""
        print("Available Additional Features:")
        for feature, cost in self.additional_features.items():
            print(f"{feature}: ${cost}")

    def display_message_multiple_members(self):
        """Function message multiple members"""
        print("Apply 10% discount for group memberships")

    def select_membership_plan(self, plan_name, num_members=1):
        """Function select membership plan"""
        if plan_name in self.membership_plans:
            self.selected_plan = plan_name
            self.num_members = num_members
        else:
            raise ValueError("Invalid membership plan selected.")

    def add_additional_features(self, features):
        """Function add additional features"""
        for feature in features:
            feature = feature.title()
            if feature in self.additional_features:
                self.selected_features.append(feature)
            else:
                raise ValueError("Invalid feature selected")

    def get_discount(self):
        """Function get discount"""
        if self.total_cost > 400:
            self.total_discount = 50
        elif self.total_cost > 200:
            self.total_discount = 20
        else:
            self.total_discount = 0
        self.total_cost -= self.total_discount


    def premiun_membership(self):
        """Function apply an additional 15% in plan premium"""
        self.total_cost = self.total_cost * 1.15

    def calculate_cost(self):
        """Function calculate cost"""
        if not self.selected_plan:
            raise ValueError("No membership plan selected.")

        base_cost = self.membership_plans[self.selected_plan]['cost']
        additional_features_cost = sum(
            self.additional_features[feature] for feature in self.selected_features
        )

        cost_members = base_cost * self.num_members
        self.total_cost = cost_members + (additional_features_cost * self.num_members)

        if self.num_members >= 2:
            self.total_cost *= 0.9  # Apply 10% discount for group memberships

        self.get_discount()

        if self.selected_plan == 'Premium':
            self.premiun_membership()

        return self.total_cost

    def is_available_plan(self):
        """Function is available plan"""
        if not self.membership_plans[self.selected_plan]['available']:
            print(f"Error: The selected membership plan '{self.selected_plan}' is unavailable.")
            return False
        return True

    def is_available_features(self):
        """Function is available features"""
        for feature in self.selected_features:
            if feature not in self.additional_features:
                print(f"Error: The selected feature '{feature}' is unavailable.")
                return False
        return True

    def display_membership_confirmation(self):
        """Function display_membership_confirmation"""
        self.calculate_cost()
        print("\nMembership Confirmation:")
        print(f"Selected Plan: {self.selected_plan}")
        print(f"Number of Members: {self.num_members}")
        if self.selected_features:
            print(f"Additional Features: {', '.join(self.selected_features)}")
        print(f"Total Discount Applied: ${self.total_discount:.2f}")
        print(f"Total Cost: ${self.total_cost:.2f}")

    def confirm_membership(self):
        """Function confirm membership"""
        self.calculate_cost()
        print("Membership Confirmation:")
        print(f"Selected Plan: {self.selected_plan}")
        print(f"Number of Members: {self.num_members}")
        print(f"Additional Features: {', '.join(self.selected_features)}")
        print(f"Total Discount Applied: ${self.total_discount:.2f}")
        print(f"Total Cost: ${self.total_cost:.2f}")

        confirmation = input("Do you confirm this membership? (y/n): ")
        if confirmation.lower() == 'y':
            return self.total_cost
        else:
            print("Membership selection canceled.")
            return -1

    def run(self):
        """ Run program """
        while True:
            try:
                self.display_membership_plans()
                plan = input("Select a membership plan: ").capitalize()
                self.display_message_multiple_members()
                num_members = int(input("Enter the number of members: "))
                self.select_membership_plan(plan, num_members)

                if not self.is_available_plan():
                    continue

                add_features = input("Do you want to add additional features? (y/n): ")
                if add_features.lower() == 'y':
                    self.display_additional_features()
                    message_feature = "Enter the feature numbers you want to add (comma separated):"
                    features = input(message_feature).split(', ')
                    self.add_additional_features(features)

                if not self.is_available_features():
                    continue

                self.display_membership_confirmation()

                confirmation = input("Do you confirm this membership? (y/n): ").lower()
                if confirmation == 'y':
                    return self.confirm_membership()
                else:
                    print("Membership selection canceled. Please make changes to your selections.")
                    continue  # Repeat the loop to allow changes

            except ValueError as e:
                print(f"Error: {e}")
                continue

if _name_ == "_main_":
    gym = GymMembership()
    total_cost = gym.run()
    if total_cost != -1:
        print(f"Final Membership Cost: ${total_cost:.2f}")
    else:
    else:
        print("Membership selection was canceled or invalid.")