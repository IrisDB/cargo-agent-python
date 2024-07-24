# Cargo Agent Python

The cargo agent is an integrated analysis sub-module for MoveApps. It is executed on the data output after each run of an App and provides the user with a quick overview of the output that has been created by an App. It is indicated by a green 'bobble' on the top-right corner of an App container and can be opened by clicking on it. Usually, it gives an overview of the number of animals, tracks and locations, the time interval, bounding box and attribute names. Depending on the output type of an App, these properties can differ. 

When a new IO type is requested for MoveApps for the first time, the person submitting it is required to provide cargo agent analysis code that produces a list of summary properties that MoveApps can print as a json overview of the most important properties of the data type, so that anyone using Apps with this IO type as output can quickly evaluate obtained results. Please follow the steps below to create it.

## How to request a new IO type?

### 1. Prepare your new MoveApps IO type

1. What is a good **title** for the IO type?
Provide a sensible label for the IO type that you request. Please follow our convention to include the package name and class name like `MovingPandas.TrajectoryCollection`. This title is intended for MoveApps users.
1. What is a good **slug** for the IO type? Your IO type must be referenced in a file-path-save way. For example a slug for the label `MovingPandas.TrajectoryCollection` could be `moving_pandas_trajectory_collection`. This slug is intended for other App developers and MoveApps-intern file paths.
1. What is the **file-extension** of this IO type?
Provide the extension of the file by which the new IO type can be transferred to the user during download. This file-extension is intended for MoveAppy users. In Python, the recommended file extension is pickle.

Summary:

- Title (referenced in the following document as `{IO_TYPE_TITLE}`)
- Slug (`{IO_TYPE_SLUG}`)
- File-Extension (`{IO_TYPE_FILE_EXTENSION}`)

### 2. Fork this repository

Please do not work on our `main` branch, but fork the repository and add files that are necessary to extend MoveApps by your requested IO type. After that, submit a **Pull-Request** to this repository with your changes. See below for details of the necessary files: 

- analyzer code
- example data
- documentation
- unit tests

### 3. Add analysis code for the IO type overview

Location: `src/analyzer/{IO_TYPE_SLUG}/analyzer.py`

Implement code by extending the base class `src/analyzer/base_analyzer.py` to extract a useful list of overview properties of your new IO type. Make sure that a proper list of useful information is created by your code (with useful keys). At the end this list will be serialized by `json` and presented to any MoveApps user that runs Apps of this new IO (output) type in a workflow.

<details>
    <summary>An example output of a (serialized json) list</summary>

```
[
    {
        "positions_total_number": 3243
    },
    {
        "timestamps_range": [
            "2021-07-01 06:40:00",
            "2022-03-15 14:13:00"
        ]
    },
    {
        "animals_total_number": 1
    },
    {
        "animal_names": [
            "Goat-8810"
        ]
    },
    {
        "taxa": [
            "Capra hircus"
        ]
    },
    {
        "sensor_types": [
            "GPS"
        ]
    },
    {
        "positions_bounding_box": {
            "x_min": 14.9216333333333,
            "y_min": 37.8303666666667,
            "x_max": 14.9606333333333,
            "y_max": 37.8717833333333
        }
    },
    {
        "projection": "EPSG:4326"
    },
    {
        "tracks_total_number": 1
    },
    {
        "track_names": [
            "Goat.8810..deploy_id.1600804509."
        ]
    },
    {
        "number_positions_by_track": {
            "Goat.8810..deploy_id.1600804509.": 3243
        }
    },
    {
        "data_attributes": [
            "sensor_type_id",
            "comments",
            "data_decoding_software",
            "gps_horizontal_accuracy_estimate",
            "gps_speed_accuracy_estimate",
            "gps_time_to_fix",
            "ground_speed",
            "heading",
            "height_above_ellipsoid",
            "icarus_ecef_vx",
            "icarus_ecef_vy",
            "icarus_ecef_vz",
            "icarus_ecef_x",
            "icarus_ecef_y",
            "icarus_ecef_z",
            "icarus_reset_counter",
            "icarus_timestamp_accuracy",
            "icarus_timestamp_source",
            "icarus_uplink_counter",
            "import_marked_outlier",
            "location_error_text",
            "manually_marked_outlier",
            "mortality_status",
            "sequence_number",
            "sigfox_rssi",
            "tag_voltage",
            "timestamp",
            "transmission_protocol",
            "transmission_timestamp",
            "event_id",
            "visible",
            "individual_name_deployment_id",
            "deployment_id",
            "tag_id",
            "individual_id",
            "animal_life_stage",
            "animal_reproductive_condition",
            "attachment_type",
            "deploy_off_timestamp",
            "deploy_on_person",
            "deploy_on_timestamp",
            "sensor_type_ids",
            "capture_location",
            "deploy_on_location",
            "deploy_off_location",
            "nick_name",
            "ring_id",
            "sex",
            "taxon_canonical_name",
            "individual_number_of_deployments",
            "mortality_location",
            "tag_local_identifier",
            "tag_number_of_deployments",
            "study_id",
            "acknowledgements",
            "citation",
            "grants_used",
            "has_quota",
            "i_am_owner",
            "is_test",
            "license_terms",
            "license_type",
            "name",
            "study_number_of_deployments",
            "number_of_individuals",
            "number_of_tags",
            "principal_investigator_name",
            "study_objective",
            "study_type",
            "suspend_license_terms",
            "i_can_see_data",
            "there_are_data_which_i_cannot_see",
            "i_have_download_access",
            "i_am_collaborator",
            "study_permission",
            "timestamp_first_deployed_location",
            "timestamp_last_deployed_location",
            "number_of_deployed_locations",
            "taxon_ids",
            "contact_person_name",
            "main_location",
            "individual_local_identifier",
            "timestamp_tz",
            "geometry"
        ]
    },
    {
        "n": "non-empty-result"
    }
]
```
</details>

### 4. Add documentation about the requested IO type

Location: `src/analyzer/{IO_TYPE_SLUG}/README.md`

Please document your IO type. If publicly available documentation for your IO type already exist feel free to provide a link to this document in the `README.md`.

### 5. Add test input data of the requested IO type

Location: `test/resources/{IO_TYPE_SLUG}/some_file_name.{IO_TYPE_FILE_EXTENSION}`

Example data of a new IO type are useful to understand their uses and properties. Provide 2-3 example files that properly work with your cargo agent analyser code.

### 6. Add unit tests

Location: `test/analyzer/{IO_TYPE_SLUG}/test_analyzer.py`

Unit tests ensure that edge cases are considered sufficiently by open code like the cargo agent of a new IO type. This code needs to run properly, as it is used within the MoveApps system each time an App with the respective IO type as output is run. Please include unit tests for all simple edge cases. If you are unsure, have a look at test files of other IO types.

### 7. Create a pull request

After you have created a pull request to our GitHub repository, our administrators will evaluate all files and get back to you with comments and/or approve the new IO type by merging your branch. Finally, our GitHub workflow will execute all tests and initialise the build of a Docker image.

### 8. Request the new IO type on MoveApps

With the pull request link from above, you are able to request the IO type on MoveApps. This can be done during _initialization_ of a new App at MoveApps and following the link for _requesting a new IO type_. You need the information from the _first step of this document (Preparation)_ and the link to your _Pull Request_.

## How to run the complete cargo-agent locally (e2e)

1. Open `main.py` and adjust `dev_analyze_file`. This file will be analyzed.
2. Run `main.py`
3. The cargo-agent listens now to an added or modified file named by 1.: `INFO: init for /opt/couchbits/projects/max-planck-gesellschaft/moveapps/apps/cargo-agent-python/resources/raw/input2_LatLon.pickle`
4. Now insert or modify this file (eg. by `touch resources/raw/input2_LatLon.pickle`): `INFO: output-file change detected!`
5. The result json file content will be printed and persisted in `resources/result/result.json`