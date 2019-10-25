package ru.deliveryClub;
/*
Created by Kavalerov
*/

import org.junit.Assert;
import org.junit.Test;

public class FirstTest extends WebDriverSettings {

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
}