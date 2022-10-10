import { ApolloClient, createHttpLink, InMemoryCache } from "@apollo/client";


const httpLink =  createHttpLink({
  uri: "http://127.0.0.1:8001/graphql",
});


export const client = new ApolloClient({
  link: httpLink,
  cache: new InMemoryCache(),
  connectToDevTools: true
});
