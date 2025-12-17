/**
 * Représente un livre doté de propriétés mystiques.
 */
public class LivreMagique {
    private String titre;
    private int pointsDeMagie;

    /**
     * Constructeur pour initialiser le livre
     */
    public LivreMagique(String unTitre, int magieInitiale) {
        this.titre = unTitre;
        this.pointsDeMagie = magieInitiale;
    }
    
    public String getTitre() {
        return titre;
    }

    public int getPointsDeMagie() {
        return pointsDeMagie;
    }

    /**
     * Méthode qui manipule les attributs 
     * Cette méthode "enchanter" augmente la puissance du livre.
     */
    public void enchanter() {
        this.pointsDeMagie = this.pointsDeMagie + 10;
    }
}