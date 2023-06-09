public class bola {
    private String material;
    private String cor;
    private int tamanho;
    private boolean cheia;
    
    public bola() {};
    public bola(String material, String cor, int tamanho, boolean cheia) {
        this.material = material;
        this.cor = cor;
        this.tamanho = tamanho;
        this.cheia = cheia;
    };
    public bola(String cor, int tamanho) {
        this.cor = cor;
        this.tamanho = tamanho;
    };
    
    public void setBola(String material, String cor, int tamanho, boolean cheia){
        this.material = material;
        this.cor = cor;
        this.tamanho = tamanho;
        this.cheia = cheia;
    }
    
    public void getBola(){
        System.out.println("Material: " + material);
        System.out.println("Cor: " + cor);
        System.out.println("Tamanho: " + tamanho);
        System.out.println("Esta cheia ? " + cheia);
    } 
    
    public void pintar(String cor){
        this.cor = cor;
    }
    
    public void encher(boolean cheia) {
        this.cheia = cheia;
    }
    
    public void esvaziar(boolean cheia) {
        this.cheia = cheia;
    }
}