package org.parcore.api.client.endpoints;

import org.parcore.api.client.async.ApiCallback;
import org.parcore.api.client.utilities.ApiException;
import org.parcore.domain.FileFormat;
import org.parcore.domain.FileFormats;

/**
 * PAR API
 * <p>
 * FileFormatsApi
 * <p>
 * Client interface for the File Formats PAR Core Entity endpoint
 * <p>
 * OpenAPI spec version: 1.0.0
 * <p>
 * This class is based on code auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 */
@SuppressWarnings("unused")
public interface FileFormatsApi {

    /**
     * Retrieve all file formats
     * Allow to retrieve the details of all the file formats
     *
     * @param returnSubEntities Specify if sub entities should be included in response. (optional)
     * @return FileFormats wrapper of all formats
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    FileFormats getAllFileFormats(Boolean returnSubEntities) throws ApiException;

    /**
     * Retrieve a paged list of File Formats
     *
     * @param returnSubEntities Specify if sub entities should be included in response. (optional)
     * @param offset            Offset from which to start the list
     * @param limit             Maximum number of formats to return
     * @return FileFormats wrapper of up to limit formats
     * @throws ApiException On error
     */
    FileFormats getPagedListOfFileFormats(Boolean returnSubEntities, Integer offset, Integer limit) throws ApiException;

    /**
     * Retrieve a list of file formats modified between the two specified dates
     *
     * @param returnSubEntities Specify if sub entities should be included in response. (optional)
     * @param modifiedAfter     Filter the file formats to return only the ones having a localLastModifiedDate value GREATER than the one passed in. Allowed datetime formats are YYYY-MM-DD\\&#39;T\\&#39;hh\\:mm\\:ssTZD and YYYY-MM-DD. In the second scenario, when the time is not provided, it will be assumed to be 00\\:00\\:00 UTC time. (optional)
     * @param modifiedBefore    Filter the file formats to return only the ones having a localLastModifiedDate value LOWER than the one passed in. Allowed datetime formats are YYYY-MM-DD\\&#39;T\\&#39;hh\\:mm\\:ssTZD and YYYY-MM-DD. In the second scenario, when the time is not provided, it will be assumed to be 00\\:00\\:00 UTC time (optional)
     * @return FileFormats wrapper of the formats
     * @throws ApiException On error
     */
    FileFormats getFileFormatsByModifiedDates(Boolean returnSubEntities, String modifiedAfter, String modifiedBefore) throws ApiException;

    /**
     * Retrieve a paged list of file formats modified between given dates
     *
     * @param returnSubEntities Specify if sub entities should be included in response. (optional)
     * @param modifiedAfter     Filter the file formats to return only the ones having a localLastModifiedDate value GREATER than the one passed in. Allowed datetime formats are YYYY-MM-DD\\&#39;T\\&#39;hh\\:mm\\:ssTZD and YYYY-MM-DD. In the second scenario, when the time is not provided, it will be assumed to be 00\\:00\\:00 UTC time. (optional)
     * @param modifiedBefore    Filter the file formats to return only the ones having a localLastModifiedDate value LOWER than the one passed in. Allowed datetime formats are YYYY-MM-DD\\&#39;T\\&#39;hh\\:mm\\:ssTZD and YYYY-MM-DD. In the second scenario, when the time is not provided, it will be assumed to be 00\\:00\\:00 UTC time (optional)
     * @param offset            Offset from which to start the list
     * @param limit             Maximum number of formats to return
     * @return FileFormats wrapper of up to limit formats modified between the specified dates
     * @throws ApiException On error
     */
    FileFormats getPagedListOfFileFormatsByModifiedDates(Boolean returnSubEntities, String modifiedAfter, String modifiedBefore, Integer offset, Integer limit) throws ApiException;

    /**
     * Retrieve all file formats (asynchronously)
     * Allow to retrieve the details of all the file formats
     *
     * @param returnSubEntities Specify if sub entities should be included in response. (optional)
     * @param modifiedAfter     Filter the file formats to return only the ones having a localLastModifiedDate value GREATER than the one passed in. Allowed datetime formats are YYYY-MM-DD\\&#39;T\\&#39;hh\\:mm\\:ssTZD and YYYY-MM-DD. In the second scenario, when the time is not provided, it will be assumed to be 00\\:00\\:00 UTC time. (optional)
     * @param modifiedBefore    Filter the file formats to return only the ones having a localLastModifiedDate value LOWER than the one passed in. Allowed datetime formats are YYYY-MM-DD\\&#39;T\\&#39;hh\\:mm\\:ssTZD and YYYY-MM-DD. In the second scenario, when the time is not provided, it will be assumed to be 00\\:00\\:00 UTC time (optional)
     * @param callback          The callback to be executed when the API call finishes
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     */
    void getFileFormatsAsync(Boolean returnSubEntities, String modifiedAfter, String modifiedBefore, final ApiCallback<FileFormats> callback) throws ApiException;

    /**
     * Create a new file format. The newly created FileFormat is returned by the request.
     * Create a new file format with the data provided in the body of the request. The only field that is always required is the file format that has to be created. If the body is not provided with the desired puid for the new file format, then the next available puid in the database will be used.
     *
     * @param data              (required)
     * @param returnSubEntities Specify if sub entities should be included in response. (optional)
     * @return FileFormat
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    FileFormat createFileFormat(FileFormat data, Boolean returnSubEntities) throws ApiException;

    /**
     * Create a new file format (asynchronously)
     * Create a new file format with the data provided in the body of the request. The only field that is always required is the file format that has to be created. If the body is not provided with the desired puid for the new file format, then the next available puid in the database will be used.
     *
     * @param data              (required)
     * @param returnSubEntities Specify if sub entities should be included in response. (optional)
     * @param callback          The callback to be executed when the API call finishes
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     */
    void createFileFormatAsync(FileFormat data, Boolean returnSubEntities, final ApiCallback<FileFormat> callback) throws ApiException;

    /**
     * Retrieve a file format by its PUID
     * Allow to retrieve the details of the specific file format provided in the url.
     *
     * @param puid              Unique identifier for the file format to retrieve. (required)
     * @param returnSubEntities Specify if sub entities should be included in response. (optional)
     * @return FileFormat
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    FileFormat getFileFormatByPuid(String puid, Boolean returnSubEntities) throws ApiException;

    /**
     * Retrieve a file format (asynchronously)
     * Allow to retrieve the details of the specific file format provided in the url.
     *
     * @param puid              Unique identifier for the file format to retrieve. (required)
     * @param returnSubEntities Specify if sub entities should be included in response. (optional)
     * @param callback          The callback to be executed when the API call finishes
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     */
    void getFileFormatByPuidAsync(String puid, Boolean returnSubEntities, final ApiCallback<FileFormat> callback) throws ApiException;

    /**
     * Update an existing file format. The newly updated FileFormat is returned by the request
     * Allow to apply the changes specified int the body to the file format provided in the url.
     *
     * @param puid              Unique identifier for the file format to update (required)
     * @param data              (required)
     * @param returnSubEntities Specify if sub entities should be included in response. (optional)
     * @return FileFormat
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    FileFormat updateFileFormat(String puid, FileFormat data, Boolean returnSubEntities) throws ApiException;

    /**
     * Update an existing file format (asynchronously)
     * Allow to apply the changes specified int the body to the file format provided in the url.
     *
     * @param puid              Unique identifier for the file format to update (required)
     * @param data              (required)
     * @param returnSubEntities Specify if sub entities should be included in response. (optional)
     * @param callback          The callback to be executed when the API call finishes
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     */
    void updateFileFormatAsync(String puid, FileFormat data, Boolean returnSubEntities, final ApiCallback<FileFormat> callback) throws ApiException;
}
