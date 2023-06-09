package generica;

public class Animal {
    private String nome;
    private String cor;
    private String tipo;
    
    Animal(String nome, String cor, String tipo) {
        this.cor = cor;
        this.nome = nome;
        this.tipo = tipo;
    };

    public String get() {
        return nome + "/" + cor + "/" + tipo;
    };

}
