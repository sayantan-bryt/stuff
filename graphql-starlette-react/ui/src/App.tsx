import "./App.css";
import { client } from "./ApolloClient/client";
import { ApolloProvider } from '@apollo/client';
import { BooksPage } from './BooksPage';

const App = () => {
  return (
    <ApolloProvider client={client}>
      <div className="App">
        <BooksPage />
      </div>
    </ApolloProvider>
  );
}

export default App;
