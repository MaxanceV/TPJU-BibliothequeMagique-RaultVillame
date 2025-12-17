from behave import given, when, then
from magicien import Magicien
from livre_magique import LivreMagique

@given('un magicien nommé {nom}')
def step_impl(context, nom):
    context.magicien = Magicien(nom)

@given('un livre nommé {titre} avec {points:d} points de magie')
@given('un livre nommé "{titre}" avec {points:d} points de magie')
def step_impl(context, titre, points):
    # Cette étape gère les deux formats (avec ou sans guillemets)
    context.livre = LivreMagique(titre, points)

@when('{nom} prend le livre')
def step_impl(context, nom):
    context.magicien.prendre_livre(context.livre)

@then('sa puissance de sort doit être de {total:d}')
def step_impl(context, total):
    assert context.magicien.puissance_totale == total

@when('un magicien enchante le livre')
def step_impl(context):
    context.livre.enchanter()

@then('le livre doit posséder {resultat:d} points de magie')
def step_impl(context, resultat):
    assert context.livre.get_points_de_magie == resultat