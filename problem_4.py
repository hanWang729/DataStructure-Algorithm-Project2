class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
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

print(is_user_in_group(sub_child_user, parent))
print(is_user_in_group(sub_child_user, child))
print(is_user_in_group(sub_child_user, sub_child))

print(is_user_in_group(sub_child_user2, parent))
print(is_user_in_group(sub_child_user2, child))
print(is_user_in_group(sub_child_user2, sub_child))