// screens/HomeScreen.js
import React from 'react';
import { View, Text, StyleSheet, FlatList, TouchableOpacity } from 'react-native';
import styles from '../styles/styles.js';
import mockData from './assets/mock_data.json'

const products = [
  {"id": "0", "nome": "Artemide", "inizio": "2000-01-01", "fine": "2002-12-31", "budget": "255000"},
  {"id": "1", "nome": "Pegasus", "inizio": "2012-01-01", "fine": "2014-12-31", "budget": "330000"},
  {"id": "2", "nome": "WineSharing", "inizio": "1999-01-01", "fine": "2003-12-31", "budget": "998000"},
  {"id": "3", "nome": "Simap", "inizio": "2010-02-01", "fine": "2014-03-17", "budget": "158000"},
  {"id": "4", "nome": "DropDiscovery", "inizio": "2010-09-13", "fine": "2013-01-20", "budget": "99000"}
];

function HomeScreen({ navigation }) {

  /*const [data,setData]=useState(null);
    /*const [headers, setHeaders]=useState([]);
  
  const fetchData=async(endpoint)=>{
    try{
      const response=await axios.get(`${SERVER_URL}${endpoint}`);
      setData(response.data);
      if(response.data.length>0){
        /*setHeaders(Object.keys(response.data[0]));
      }
    }catch(err){
      console.error("Errore nella richiesta:",err);
      const dataset=mockData[endpoint.replace("/","")];
      setData(dataset);
      if(dataset.length>0){
        /*setHeaders(Object.keys(dataset[0]));
      }
    }
  };*/




  const renderItem = ({ item }) => (
    <TouchableOpacity
      style={styles.productCard}
      onPress={() => navigation.navigate('TableView', { productId: item.id })}
    >
      <Text style={styles.productName}>{item.name}</Text>
      <Text style={styles.productPrice}>{item.price}</Text>
    </TouchableOpacity>
  );

  return (
    <View style={styles.container}>
      <Text style={styles.title}>I Nostri Prodotti</Text>
      <FlatList
        data={products}
        renderItem={renderItem}
        keyExtractor={item => item.id}
        contentContainerStyle={styles.productList}
      />
    </View>
  );
}

export default HomeScreen;