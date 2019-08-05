package com.oop;

public class Main {
    public static void main(String[] args) {

        System.out.println("Сейчас собак "+Dog.getDogsCount());

        Dog lab = new Dog();
        lab.setName("Charley");
        lab.setBreed("Lab");
        lab.setSize(Size.AVERAGE);
        lab.bite();

        Dog sheppard = new Dog();
        sheppard.setName("Mike");
        sheppard.setBreed("Sheppard");
        sheppard.setSize(Size.BIG);
        sheppard.bite();


        Dog doberman = new Dog();
        doberman.setName("Leonard");
        doberman.setBreed("Doberman");
        doberman.setSize(Size.BIG);
        doberman.bite();


//        System.out.println("Lab's name is "+ lab.getName());
//        System.out.println("Sheppard's name is "+ sheppard.getName());

    }
}
