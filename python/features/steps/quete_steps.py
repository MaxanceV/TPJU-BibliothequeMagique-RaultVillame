from behave import given, when, then
from Classe.Quete import Quete
from Classe.Recompense import Recompense


@given('une quete "{titre}"')
def step_impl(context, titre):
    context.quete = Quete(titre)


@given('une quete "{titre}" avec une recompense de {bonus:d} XP')
def step_impl(context, titre, bonus):
    context.quete = Quete(titre)
    context.recompense = Recompense("Bonus", bonus)
    context.quete.attribuerRecompense(context.recompense)


@when('j ajoute {points:d} points XP')
def step_impl(context, points):
    context.quete.ajouterXp(points)


@then('le XP de la quete est {xp:d}')
def step_impl(context, xp):
    assert context.quete.getXp() == xp


@then('le XP total avec bonus est {xp:d}')
def step_impl(context, xp):
    assert context.quete.xpTotalAvecBonus() == xp


@given('deux quetes "{q1}" et "{q2}"')
def step_impl(context, q1, q2):
    context.q1 = Quete(q1)
    context.q2 = Quete(q2)


@given('une recompense "{nom}" avec {bonus:d} XP')
def step_impl(context, nom, bonus):
    context.recompense = Recompense(nom, bonus)


@when('j assigne la recompense a la quete "{titre}"')
def step_impl(context, titre):
    if context.q1.getTitre() == titre:
        context.q1.attribuerRecompense(context.recompense)
    else:
        context.q2.attribuerRecompense(context.recompense)


@then('la quete "{titre}" n a pas de recompense')
def step_impl(context, titre):
    quete = context.q1 if context.q1.getTitre() == titre else context.q2
    assert quete.getRecompense() is None


@then('la recompense appartient a la quete "{titre}"')
def step_impl(context, titre):
    quete = context.q1 if context.q1.getTitre() == titre else context.q2
    assert context.recompense.getQuete() == quete
