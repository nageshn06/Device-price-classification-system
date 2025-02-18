package com.example.deviceprice.model;

import javax.persistence.Entity;
import javax.persistence.Id;

@Entity
public class Device {

    @Id
    private Long id;
    private int batteryPower;
    private int blue;
    private float clockSpeed;
    // Add other device attributes here

    // Getters and setters
}
