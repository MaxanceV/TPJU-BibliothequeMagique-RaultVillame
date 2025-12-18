from behave import given, when, then

from magicien_de_feu import MagicienDeFeu
from livre_magique_de_feu import LivreMagiqueDeFeu

@given('un magicien de feu nommé {nom}')
def step_impl(context, nom):
    context.magicien = MagicienDeFeu(nom)


@when('il invoque un livre "{titre}"')
def step_impl(context, titre):
    context.livre = context.magicien.invoquer_livre(titre)


@then('le magicien possède le livre "{titre}"')
def step_impl(context, titre):
    assert context.livre.titre == titre
    assert context.livre in context.magicien.livres
    assert context.livre.possesseur == context.magicien


@then('le magicien possède un livre de feu "{titre}"')
def step_impl(context, titre):
    assert context.livre.titre == titre
    assert isinstance(context.livre, LivreMagiqueDeFeu)
    assert context.livre in context.magicien.livres
    assert context.livre.possesseur == context.magicien
