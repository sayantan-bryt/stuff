import { useQuery } from "@apollo/client";
import { BOOKS_QUERY } from './queries';


export const BooksPage = () => {
  const { data, loading, error } = useQuery(BOOKS_QUERY);

  if (loading) {
    return <div>{loading}</div>;
  }

  if (error) {
    console.log({error});
    return <div>ERROR </div>;
  }

  console.log(data);
  return data.books.map( ({ book_name, writer } : {book_name: string, writer: string}) => (
    <div key={book_name}>
      <p>
        {book_name}: {writer}
      </p>
    </div>
  ));
}


