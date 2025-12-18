from behave import given, then
from Classe.Recompense import Recompense


@given('une récompense "{nom}" avec {bonus:d} XP')
def step_impl(context, nom, bonus):
    context.recompense = Recompense(nom, bonus)


@then('le nom de la récompense est "{nom}"')
def step_impl(context, nom):
    assert context.recompense.getNom() == nom


@then('le bonus XP est {bonus:d}')
def step_impl(context, bonus):
    assert context.recompense.getBonusXp() == bonus


@then('la récompense n\'est liée à aucune quête')
def step_impl(context):
    assert context.recompense.getQuete() is None
