import { gql } from "@apollo/client";

export const BOOKS_QUERY = gql`
    query Query {
        books {
            book_name: title
            writer: author
        }
    }
`;

