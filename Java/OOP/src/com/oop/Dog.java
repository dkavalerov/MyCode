package com.oop;

public class Dog {

    private static int dogsCount;

    private int paws;
    private int tail;
    private String name;
    private String breed;
    private String size;

    public Dog() {
        dogsCount++;
        System.out.println("Количество собак: "+dogsCount);

    }

    public static int getDogsCount() {
        return dogsCount;
    }


    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        if (size.equalsIgnoreCase("Big") ||
                size.equalsIgnoreCase("Average") ||
                size.equalsIgnoreCase("Small")) {
            this.size = size;
        } else {
            System.out.println("Размер должен быть одни из этих трех: Большой, Средний или Маленький");
        }
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setPaws(int paws) {
        if (paws == 4) {
            this.paws = paws;

        } else {
            this.paws = 4;
//            System.out.println("Введено не правильное количество лап " + paws + " для собаки");
//            System.out.println("Правильное значение 4");
//            System.out.println("Лабрадор имеет " + getPaws() + " лапы");

        }

    }

    public int getPaws() {
        return paws;
    }

    public int getTail() {
        return tail;
    }

    public void setTail(int tail) {
        if (tail == 1) {
            this.tail = tail;
        } else {
            this.tail = 1;
            System.out.println("Введено не правильное количество хвостов " + tail + " для собаки");
            System.out.println("Правильное значение 1");
        }
    }

    public String getBreed() {
        return breed;
    }

    public void setBreed(String breed) {
        this.breed = breed;
    }

    public void bark() {
        if (size.equalsIgnoreCase("Big")) {
            System.out.println("Воффф вофф!");
        } else if (size.equalsIgnoreCase("Average")) {
            System.out.println("РАфф рафф!");
        } else {
            System.out.println("Тяфффф!");
        }

    }

    public void bite() {
        if (dogsCount > 2) {
            System.out.println("Вас кусают собаки!");
        } else {
            bark();
        }


    }
}