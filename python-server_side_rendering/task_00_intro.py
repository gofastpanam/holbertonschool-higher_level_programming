#!/usr/bin/python3
"""
Creating a Simple Templating Program
"""


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Invalid template type")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict)
                                                  for item in attendees):
        print("Error: Invalid attendees type.")
        return

    if not template:
        print("Template is empty.")
        return
    if not attendees:
        print("No data provided.")
        return

    for index, attendee in enumerate(attendees, start=1):
        processed_template = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A")
            processed_template = processed_template.replace(f"{{{key}}}",
                                                            value
                                                            if value
                                                            else "N/A")

        output_filename = f"output_{index}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write(processed_template)
        print(f"Generated {output_filename}")
