from behave import given, when, then
from quete import Quete
from recompense import Recompense


@given('une quete "{titre}"')
def step_impl(context, titre):
    context.quete = Quete(titre)


@given('une quete "{titre}" avec une recompense de {bonus:d} XP')
def step_impl(context, titre, bonus):
    context.quete = Quete(titre)
    context.recompense = Recompense("Bonus", bonus)
    context.quete.attribuer_recompense(context.recompense)


@when('j ajoute {points:d} points XP')
def step_impl(context, points):
    context.quete.ajouter_xp(points)


@then('le XP de la quete est {xp:d}')
def step_impl(context, xp):
    assert context.quete.xp == xp


@then('le XP total avec bonus est {xp:d}')
def step_impl(context, xp):
    assert context.quete.xp_total_avec_bonus() == xp


@given('deux quetes "{q1}" et "{q2}"')
def step_impl(context, q1, q2):
    context.q1 = Quete(q1)
    context.q2 = Quete(q2)


@given('une recompense "{nom}" avec {bonus:d} XP')
def step_impl(context, nom, bonus):
    context.recompense = Recompense(nom, bonus)


@when('j assigne la recompense a la quete "{titre}"')
def step_impl(context, titre):
    quete = context.q1 if context.q1.titre == titre else context.q2
    quete.attribuer_recompense(context.recompense)


@then('la quete "{titre}" n a pas de recompense')
def step_impl(context, titre):
    quete = context.q1 if context.q1.titre == titre else context.q2
    assert quete.recompense is None


@then('la recompense appartient a la quete "{titre}"')
def step_impl(context, titre):
    quete = context.q1 if context.q1.titre == titre else context.q2
    assert context.recompense.quete == quete
