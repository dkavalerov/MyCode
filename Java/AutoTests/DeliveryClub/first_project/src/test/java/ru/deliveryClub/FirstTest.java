package ru.deliveryClub;
/*
Created by Kavalerov
*/

import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.chrome.ChromeDriver;

public class FirstTest {

    public ChromeDriver driver;

    @Before
    public void setUp() {
        System.setProperty("webdriver.chrome.driver", "/Users/mrxzi/Downloads/chromedriver");
        driver = new ChromeDriver();
        System.out.println("test start");

    }


    @Test
    public void firstTest() {
        driver.get("https://www.delivery-club.ru");
        String title = driver.getTitle();
        Assert.assertTrue(title.equals("«Delivery Club» — круглосуточная доставка из любимых ресторанов города"));
    }

    @Test
    public void firstTest2() {
        driver.get("https://www.delivery-club.ru");
        String title = driver.getTitle();
        Assert.assertTrue(title.equals("«Delivery Club» — круглосуточная доставка из любимых ресторанов города"));
    }

    @After
    public void close() {
        System.out.println("test close");
        driver.quit();
    }
}