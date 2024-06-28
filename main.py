""" Team 7 """

class GymMembership:
    """Gym Membership Management System"""

    def __init__(self):
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
        self.selected_features = []
      
    def display_membership_plans(self):
        """Function display membership plans"""
        print("Available Membership Plans:")
        for plan, details in self.membership_plans.items():
            print(f"{plan}: ${details['cost']} - Benefits: {', '.join(details['benefits'])}")
          
    def select_membership_plan(self, plan_name, num_members=1):
        """Function select membership plan"""
        if plan_name in self.membership_plans:
            self.selected_plan = plan_name
            self.num_members = num_members
        else:
            raise ValueError("Invalid membership plan selected.")


    def display_additional_features(self):
        """Function display additional features"""
        print("Available Additional Features:")
        for feature, cost in self.additional_features.items():
            print(f"{feature}: ${cost}")

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


    def add_additional_features(self, features):
        """Function add additional features"""
        for feature in features:
            feature = feature.title()
            if feature in self.additional_features:
                self.selected_features.append(feature)
            else:
                raise ValueError("Invalid feature selected")

if __name__ == "__main__":
    gym = GymMembership()
    total_cost = gym.run(plan_name='Basic', num_members=1,
                         selected_features=["Personal Training", "Group Classes"])
    if total_cost != -1:
        print(f"Final Membership Cost: ${total_cost:.2f}")
    else:



        print("Membership selection was canceled or invalid.")
