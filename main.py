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
