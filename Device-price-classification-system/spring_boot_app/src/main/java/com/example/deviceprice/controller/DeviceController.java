package com.example.deviceprice.controller;

import org.springframework.http.*;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

@RestController
@RequestMapping("/api/devices")
public class DeviceController {

    private final String PYTHON_API_URL = "http://localhost:5000/api/predict";

    @PostMapping("/predict/{deviceId}")
    public ResponseEntity<?> predictDevicePrice(@PathVariable Long deviceId, @RequestBody Device device) {
        // Prepare JSON body for prediction request
        String jsonRequest = "{"battery_power": " + device.getBatteryPower() +
                             ", "blue": " + device.getBlue() +
                             ", "clock_speed": " + device.getClockSpeed() +
                             "}";

        // Send request to the Python API for prediction
        RestTemplate restTemplate = new RestTemplate();
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        HttpEntity<String> entity = new HttpEntity<>(jsonRequest, headers);

        ResponseEntity<String> response = restTemplate.exchange(PYTHON_API_URL, HttpMethod.POST, entity, String.class);
        
        // Parse the predicted result and save it in the database
        String predictedPriceRange = response.getBody();
        
        // Save prediction in the database or return as part of the response
        return ResponseEntity.ok("Predicted Price Range: " + predictedPriceRange);
    }
}
