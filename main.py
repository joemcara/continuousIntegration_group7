class GymMembership:
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