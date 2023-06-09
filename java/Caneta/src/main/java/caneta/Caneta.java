
package caneta;

public class Caneta {
    private String cor;
    private String marca;
    private int tamanho;
    
    Caneta() {}

    public String getCor() {
        return cor;
    }

    public String getMarca() {
        return marca;
    }

    public int getTamanho() {
        return tamanho;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public void setTamanho(int tamanho) {
        this.tamanho = tamanho;
    }
    
    @Override
    public String toString() {
        return "Tamanho: " + tamanho + "/n" + 
               "Marca: " + marca + "/n" + 
               "Cor: " + cor; 
    }
    
}
