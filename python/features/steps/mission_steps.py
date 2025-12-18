from behave import given, when, then

from quete import Quete
from recompense import Recompense
from mission import Mission


@given('sa puissance de base est {puissance_base:d}')
def step_impl(context, puissance_base):
    context.magicien.puissance = puissance_base


@given('une quête "{titre_quete}" avec {xp:d} xp')
def step_impl(context, titre_quete, xp):
    context.quete = Quete(titre_quete)
    context.quete.ajouterXp(xp)


@given('une récompense "{nom_recompense}" donnant {bonus:d} xp')
def step_impl(context, nom_recompense, bonus):
    context.recompense = Recompense(nom_recompense, bonus)
    context.quete.attribuerRecompense(context.recompense)


@when('le magicien termine la mission')
def step_impl(context):
    context.mission = Mission(context.magicien, context.quete)
    context.mission.terminer()


@then('la puissance du magicien doit être de {puissance_attendue:d}')
def step_impl(context, puissance_attendue):
    assert context.magicien.puissance == puissance_attendue
