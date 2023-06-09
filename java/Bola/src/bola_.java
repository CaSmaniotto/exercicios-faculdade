public class bola_ {
    
    private String material;
    private String cor;
    private int tamanho;
    private boolean cheia;
    
    public bola_() {};
    public bola_(String material, String cor, int tamanho, boolean cheia) {
        this.material = material;
        this.cor = cor;
        this.tamanho = tamanho;
        this.cheia = cheia;
    };
    public bola_(String cor, int tamanho) {
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
    
    public void encher() {
        cheia = true;
    }
    
    public void esvaziar() {
        cheia = false;
    }

    public static void main(String[] args) {
        String m = "Borracha";
        String c = "Azul";
        int t = 5;
        //boolean bool = true;
        bola b = new bola(c, t);
//      b.setBola(m,c,t,bool);
        b.getBola();
    }
}
