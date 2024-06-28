""" Team 7 """
class GymMembership:
    """Gym Membership Management System"""

    def __init__(self):
        self.additional_features = {
            'Personal Training': 25,
            'Group Classes': 15
        }
        self.selected_features = []

    def display_additional_features(self):
        """Function display additional features"""
        print("Available Additional Features:")
        for feature, cost in self.additional_features.items():
            print(f"{feature}: ${cost}")


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
