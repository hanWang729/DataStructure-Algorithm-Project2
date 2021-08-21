class Group(object):
    def __init__(self, _name):
        if _name == "" or _name is None:
            _name = "Default_Group_Name"
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        if group == "" or group is None:
            print("Error, group is empty or None")
            return
        self.groups.append(group)

    def add_user(self, user):
        if user == "" or user is None:
            print("Error, user is empty or None")
            return
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.users:
        return True
    if group.groups is None:
        return False
    for g in group.groups:
        b = is_user_in_group(user, g)
        if b is True:
            return True
    return False


# Test 1: normal test
def test1():
    print("----------------------Test 1---------------------------")
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")
    sub_child2 = Group("subchild2")

    sub_child_user = "sub_child_user"
    sub_child_user2 = "subc2"
    sub_child.add_user(sub_child_user)
    sub_child2.add_user(sub_child_user2)

    child.add_group(sub_child)
    parent.add_group(child)
    parent.add_user(sub_child_user2)

    print(is_user_in_group(sub_child_user, parent))  # True
    print(is_user_in_group(sub_child_user, child))  # True
    print(is_user_in_group(sub_child_user, sub_child))  # True

    print(is_user_in_group(sub_child_user2, parent))  # True
    print(is_user_in_group(sub_child_user2, child))  # False
    print(is_user_in_group(sub_child_user2, sub_child))  # False


#Test 2: user name is empty
def test2():
    print("----------------------Test 2---------------------------")
    sub_child = Group("subchild")
    sub_child_user = ""
    sub_child.add_user(sub_child_user)  # Print error
    print(is_user_in_group(sub_child_user, sub_child))  # False


# Test 3: generate a group with empty name
def test3():
    print("----------------------Test 3---------------------------")
    parent = Group("")  # Print error and set the group name to default name
    print(type(parent))  # It is still a Group
    user = "user"
    parent.add_user(user)
    print(is_user_in_group(user, parent)) # True, but the group name is default name


test1()
test2()
test3()
