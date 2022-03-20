import * as React from 'react';
import { useState, useEffect } from "react";
import { Center, Text, View, Image, VStack, HStack } from 'native-base';
import { weather_styles } from '../general-screens/GeneralStyle';

interface WeatherInfo {
    temperature: number
    humidity: number
    conditions: string
    wind: number
}

function Weather({ temperature, humidity, conditions, wind }: WeatherInfo) {
    if(!conditions) {
        return (
            <View style={weather_styles.background}>
                <Text style={weather_styles.header}> Cannot fetch weather data </Text>
            </View>
        );
    }

    return (
        <View style={weather_styles.background}>
            <Center>
                <VStack space={3}>
                    <Text style={weather_styles.header}> {conditions} </Text>
                    <Text style={weather_styles.header}> {temperature}°C </Text>
                    <HStack space={3}>
                        <Image style={weather_styles.img} source={require('../image/wind.png')} alt="wind" />
                        <Text style={weather_styles.header}> Wind | {Math.round(wind * 3.6)}km/h </Text>
                    </HStack>
                    <HStack space={3}>
                        <Image style={weather_styles.img} source={require('../image/hum.png')} alt="hum" />
                        <Text style={weather_styles.header}> Hum | {humidity}% </Text>
                    </HStack>
                </VStack>
            </Center>
        </View>
    );
}

const API_KEY = "650d3ff9343217c83124e2260bad673d";

export const WeatherComponent = function (): JSX.Element {
    const [weather, setWeather] = useState({ temp: 0.0, humidity: 0, conditions: '', wind: 0 });

    useEffect(() => {
        fetch(
            `http://api.openweathermap.org/data/2.5/weather?lat=51.752&lon=19.4518&APPID=${API_KEY}&units=metric`
        ).then(res => res.json()
        ).then(json => {
            if (json.cod == 200) {
                setWeather({
                    temp: json['main']['temp'],
                    humidity: json['main']['humidity'],
                    conditions: json['weather'][0]['description'],
                    wind: json['wind']['speed']
                });
            }
        });
    }, []);

    return (
        <View>
            <Weather
                temperature={weather.temp}
                humidity={weather.humidity}
                conditions={weather.conditions}
                wind={weather.wind}
            />
        </View>
    );
}
