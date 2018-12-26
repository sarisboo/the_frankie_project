from frankie import frankie
import sys


def main():
    limit = 10
    page_number = 1
    dest_path = sys.argv[1] if len(sys.argv) > 1 else "downloads"

    while page_number < limit:
        links = frankie.retrieve_episode_links(page_number)

        for link in links:
            mp3_url = frankie.retrieve_episode_url(link)

            if mp3_url != None:
                frankie.download_url(dest_path, mp3_url, link)

        page_number += 1


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
