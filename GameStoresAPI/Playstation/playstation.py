import bs4
from GameStoresAPI.Shared.shared import Shared

class Playstation:

    @staticmethod
    def url_encode(input):
        """Format a game name string so it's suitable for use on Playstation store"""
        # https://stackoverflow.com/questions/6182356/what-is-2c-in-a-url
        output = input
        replace_with_space = [" ", "&", "="]
        for replace_char in replace_with_space:
            output = output.replace(replace_char, "%20")
        return output

    @staticmethod
    def format_url(content_type, platform, query, page_number=1, region="en-gb"):
        """Format URL"""

        url = "https://store.playstation.com/{}/grid/search-game/{}?".format(region, page_number)

        final_content_type = None
        final_platform = None
        # final_query = None

        if content_type is not None:
            final_content_type = "gameContentType="
            for content in content_type:
                if content in valid_content_types:
                    final_content_type += content + ","
                else:
                    print("Content type '{}' is invalid".format(content))

            if final_content_type == "gameContentType=":
                # Meaning all entered content types were invalid
                final_content_type = None

        if platform is not None:
            final_platform = "platform="
            for system in platform:
                if system in valid_platforms:
                    final_platform += system + ","
                else:
                    print("Platform '{}' is invalid".format(system))

            if final_platform == "platform=":
                final_platform = None

        final_url = ""
        if final_content_type is not None:
            final_url += final_content_type[:-1] + "&"

        if final_platform is not None:
            final_url += final_platform[:-1] + "&"

        final_url += "query=" + url_encode(query)
        return url + final_url

    @staticmethod
    def get_data(url):
        """Get data about the games (price, name, thumbnail, etc) from search results"""

        # TODO decide how to handle results with multiple pages (currently the other pages are ignored)

        base_data = bs4.BeautifulSoup(Shared.get_page_raw(url), "html.parser")

        game_data_list = []

        if base_data.text == "Error":
            print("Error occured whilst getting data")
        else:
            item_count = len(base_data.select('div[class="ember-view"] div[class="grid-cell__title"]'))

            if item_count == 0:
                print("No Search Results")
                return "Empty"

            for i in range(0, item_count):
                title_id = base_data.select('div[class="ember-view"] div[class="grid-cell__body"]'
                                            )[i].find("a").attrs['href']

                title = base_data.select('div[class="ember-view"] div[class="grid-cell__body"]'
                                         )[i].select('div[class="grid-cell__title"]')[0].text

                if base_data.select('div[class="ember-view"] div[class="grid-cell__body"]')[i].select(
                        'h3[class="price-display__price"]'):
                   price = base_data.select('div[class="ember-view"] div[class="grid-cell__body"]')[i].select(
                       'h3[class="price-display__price"]')[0].text
                else:
                    # Price doesn't exist in typical form
                    if base_data.select('div[class="ember-view"] div[class="grid-cell__body"]')[i].select(
                            'div[class="grid-cell__ineligible-reason"]'):
                        price = base_data.select('div[class="ember-view"] div[class="grid-cell__body"]')[i].select(
                            'div[class="grid-cell__ineligible-reason"]')[0].text.strip().replace("\n", "")

                    elif base_data.select('div[class="ember-view"] div[class="grid-cell__body"]')[i].select(
                            'div[class="grid-cell__left-detail grid-cell__left-detail--detail-2"]'):
                        price = base_data.select('div[class="ember-view"] div[class="grid-cell__body"]')[i].select(
                            'div[class="grid-cell__left-detail grid-cell__left-detail--detail-2"]')[0].text
                        if price == "Full Game":
                            price = "Unknown"

                    else:
                        price = "Unknown"

                platforms = base_data.select('div[class="ember-view"] div[class="grid-cell__body"]')[i].select(
                    'div[class="grid-cell__left-detail grid-cell__left-detail--detail-1"]')[0].text

                img = base_data.select('div[class="ember-view"] div[class="grid-cell__thumbnail"]')[i].select(
                    'div[class="product-image__img product-image__img--main"]')[0].find("img").attrs['src']

                this_data = {title: {"price": price, "id": title_id, "platforms": platforms, "img": img}}
                game_data_list.append(this_data)

        return game_data_list

    @staticmethod
    def get_page_data(url):
        """Get data from the store page of a game such as price, addons, themes, extras and bundles"""

        """
        The page element '<div class="sku-info"> contains pricing and platform data
        '<div class="tech-specs"> contains genre, audio and subtitle language and file size info
        """

        base_data = bs4.BeautifulSoup(Shared.get_page_raw(url), "html.parser")

        if base_data.text == "Error":
            print("Error occured whilst getting data")
            return "Error"
        else:
            # print("This is where the stuff happens")
            # TODO get release date
            # TODO check for div[class='price-availability'] and use

            genre = "No Data"
            subtitles = "No Data"
            audio = "No Data"
            filesize = "No Data"

            title = base_data.select('h2[class="pdp__title"]')[0].text

            price = base_data.select('div[class="sku-info"] h3[class="price-display__price"]')[0].text
            if price == "":
                price = base_data.select('h5[class="provider-info__text"] span[class="provider-info__list-item"]')[0].text
                # price = "N/A"

            platform = base_data.select('div[class="sku-info"] a[class="playable-on__buttons tiny secondary hollow button"]'
                                        )[0].text

            info = ["Genre", "Audio", "Subtitles", "File Size"]

            if base_data.select('div[class="tech-specs"]'):
                details_amount = len(base_data.select('div[class="tech-specs"] div[class="tech-specs__menu-header"]'))
                for i in range(0, details_amount):
                    detail_str = str(base_data.select('div[class="tech-specs"] div[class="tech-specs__menu-header"]'
                                                      )[i].next_element).strip()

                    if detail_str in info:
                        detail = base_data.select('div[class="tech-specs"] div[class="tech-specs__menu-header"]'
                                                  )[i].next_element.next_element.next_element.text
                        detail = detail.strip()
                        detail = detail.replace((title + "\n"), "")  # print("detail", detail)

                        if detail_str == "Genre":
                            genre = detail
                        elif detail_str == "Audio":
                            audio = detail.replace("\n", ", ")
                        elif detail_str == "Subtitles":
                            subtitles = detail.replace("\n", ", ")
                        elif detail_str == "File Size":
                            filesize = detail

            else:
                pass
                # print("NAH NO TECH SPECS MATE")

        return_data = {"title": title, "price": price, "platform": platform, "genre": genre, "audio": audio,
                       "subtitles": subtitles, "filesize": filesize}

        return return_data


valid_platforms = ["ps4", "ps3", "vita", "psp"]
# platform

valid_content_types = ["games", "bundles", "addons", "themes", "other_extras", "timed_trials"]
# gameContentType



