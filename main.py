import logging
import url_monitor as u
import sys
import utils as ut


logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    try:
        arg = sys.argv
        res = u.check_url(arg[1])
        filtered_content = ut.text_filter_based_on_key("OK", res, ":")
        if not filtered_content:
            logging.error("There was no service matching the criteria")
            sys.exit(1)
        for service in filtered_content:
            logging.info(f"Service {service} is {filtered_content[service]}")
    except Exception as e:
        logging.error("an error occurred", e)
        sys.exit(1)
