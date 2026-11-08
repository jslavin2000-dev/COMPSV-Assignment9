
class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(name + " already exists!")
        else:
            self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people:
            print("Friendship not created. " + person1_name + " doesn't exist!")
            return

        if person2_name not in self.people:
            print("Friendship not created. " + person2_name + " doesn't exist!")
            return

        if person1_name == person2_name:
            print("A person cannot be friends with themselves!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for person in self.people.values():
            friend_names = []

            for friend in person.friends:
                friend_names.append(friend.name)

            print(person.name + " is friends with: " + ", ".join(friend_names))


if __name__ == "__main__":
    network = SocialNetwork()

    # Add people
    network.add_person("Alex")
    network.add_person("Jordan")
    network.add_person("Morgan")
    network.add_person("Taylor")
    network.add_person("Casey")
    network.add_person("Riley")

    # Add friendships
    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")

    # Test missing person
    network.add_friendship("Jordan", "Johnny")

    # Test duplicate person
    network.add_person("Alex")

    # Test duplicate friendship
    network.add_friendship("Alex", "Jordan")

    # Print network
    print()
    network.print_network()

# Design Memo
#
# For this assignment, I used a graph to create a simple social
# network where people can connect with each other. I think a graph
# is the best data structure for this because social networks have
# a lot of different connections between people. Each person is
# represented as a node, and each friendship is an edge connecting
# two people. This makes it easier to show how everyone is connected.
#
# A list or tree would not work as well for this type of program.
# A list could store all the people, but it would be harder to keep
# track of their friendships. A tree is better for information that
# follows a hierarchy, like a company directory. Friendships do
# not really follow a hierarchy because people can have multiple
# connections with each other.
#
# I used an adjacency list to store the friendships because it
# is simple and does not waste space storing connections that
# do not exist. I also used a dictionary to store each person,
# which makes it easier to find someone by their name.
#
# One thing I noticed was that adding friendships is pretty
# simple, but the program needs to check if both people exist
# first. I also had to make sure duplicate friendships were not
# added. Printing the network takes more time as the number of
# people and friendships increases because the program has to
# go through everyone's friends.
#
# Overall, this assignment helped me understand how graphs can
# be used in real situations and why choosing the right data
# structure is important.
