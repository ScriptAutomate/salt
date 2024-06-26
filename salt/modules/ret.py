"""
Module to integrate with the returner system and retrieve data sent to a salt returner
"""

import salt.loader


def get_jid(returner, jid):
    """
    Return the information for a specified job id

    CLI Example:

    .. code-block:: bash

        salt '*' ret.get_jid redis 20421104181954700505
    """
    returners = salt.loader.returners(__opts__, __salt__)
    return returners[f"{returner}.get_jid"](jid)


def get_fun(returner, fun):
    """
    Return info about last time fun was called on each minion

    CLI Example:

    .. code-block:: bash

        salt '*' ret.get_fun mysql network.interfaces
    """
    returners = salt.loader.returners(__opts__, __salt__)
    return returners[f"{returner}.get_fun"](fun)


def get_jids(returner):
    """
    Return a list of all job ids

    CLI Example:

    .. code-block:: bash

        salt '*' ret.get_jids mysql
    """
    returners = salt.loader.returners(__opts__, __salt__)
    return returners[f"{returner}.get_jids"]()


def get_minions(returner):
    """
    Return a list of all minions

    CLI Example:

    .. code-block:: bash

        salt '*' ret.get_minions mysql
    """
    returners = salt.loader.returners(__opts__, __salt__)
    return returners[f"{returner}.get_minions"]()
