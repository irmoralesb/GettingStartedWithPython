import movie_service


def main():
    print_header()
    search_event_loop()


def print_header():
    print("---------------------------------")
    print("       MOVIE SEARCH APP")
    print("---------------------------------")


def search_event_loop():
    search = "ONCE_THROUGH_LOOP"

    while search != "x":
        try:
            search = input("Movie search text (x to exit): ")
            if search != "x":
                results = movie_service.find_movies(search)
                print("Found {} results.".format(len(results)))
                for r in results:
                    print("{} -- {}".format(r.year, r.title))
                print()
        except ValueError:
            print("Error: Value error is required.")
        except ConnectionError:
            print("Error: Your Network is down.")
        except Exception as x:
            print("You did it again!. {}".format(x))

    print("Exiting...")


if __name__ == '__main__':
    main()
