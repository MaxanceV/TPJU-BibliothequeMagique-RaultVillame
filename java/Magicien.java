public class Magicien {
    private String nom;
    private LivreMagique monLivre; // Association 0..1 

    public Magicien(String unNom) {
        this.nom = unNom;
        this.monLivre = null; // Mains vides au départ 
    }

    // Méthode pour relier les deux objets
    public void prendreLivre(LivreMagique livre) {
        this.monLivre = livre;
    }
    
    public int calculerPuissanceSort() {
        int baseMage = 10;
            if (this.monLivre != null) {
                // Collaboration : on récupère les points du livre 
                return baseMage + this.monLivre.getPointsDeMagie(); 
            }
        return baseMage;
    }   
}