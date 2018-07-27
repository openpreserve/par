package org.parcore.api.client.endpoints;

import org.parcore.api.client.async.ApiCallback;
import org.parcore.api.client.utilities.AbstractApiCallImpl;
import org.parcore.api.client.utilities.ApiClient;
import org.parcore.api.client.utilities.ApiException;
import org.parcore.api.client.utilities.ApiResponse;
import org.parcore.domain.Tool;
import org.parcore.domain.Tools;

import java.util.Collections;

public class ToolsApiImpl extends AbstractApiCallImpl<Tools, Tool> implements ToolsApi {


    public ToolsApiImpl(ApiClient apiClient) {
        super(apiClient, "/tools", Tools.class, Tool.class);
    }

    public ToolsApiImpl(ApiClient apiClient, String[] authNames) {
        this(apiClient);
        this.localVarAuthNames = authNames;
    }

    @Override
    public Tools getAllTools() throws ApiException {
        return getListApiResponse(null, null, null, null).getData();
    }

    @Override
    public Tools getPagedListOfTools(Integer offset, Integer limit) throws ApiException {
        return getListApiResponse(null, null, offset, limit).getData();
    }

    @Override
    public Tools getPagedListOfToolsByModifiedDate(String modifiedAfter, String modifiedBefore, Integer offset, Integer limit) throws ApiException {
        return getListApiResponse(modifiedAfter, modifiedBefore, offset, limit).getData();
    }

    @Override
    public Tools getToolsByModifiedDate(String modifiedAfter, String modifiedBefore) throws ApiException {
        return getListApiResponse(modifiedAfter, modifiedBefore, null, null).getData();
    }

    @Override
    public void getToolsAsync(String modifiedAfter, String modifiedBefore, final ApiCallback<Tools> callback) throws ApiException {
        getListingAsync(null, modifiedAfter, modifiedBefore, Collections.emptyMap(), callback);
    }

    @Override
    public Tool getToolById(String id) throws ApiException {
        return getByIdApiResponse(id).getData();
    }

    @Override
    public void getToolByIdAsync(String id, final ApiCallback<Tool> callback) throws ApiException {
        getEntityAsync(id, null, callback);
    }

    @Override
    public Tool updateTool(String id, Tool data) throws ApiException {
        return updateByIdApiResponse(id, data).getData();
    }

    @Override
    public void updateToolAsync(String id, Tool data, final ApiCallback<Tool> callback) throws ApiException {
        updateEntityAsync(id, data, callback);
    }

    @Override
    public Tool createTool(Tool data) throws ApiException {
        return createToolApiResponse(data).getData();
    }

    @Override
    public void createToolAsync(Tool data, final ApiCallback<Tool> callback) throws ApiException {
        createNewEntityAsync(data, callback);
    }

    // --- Internal methods calling down to the AbstractClass
    private ApiResponse<Tool> getByIdApiResponse(String id) throws ApiException {
        return getEntity(id, null);
    }

    private ApiResponse<Tools> getListApiResponse(String modifiedAfter, String modifiedBefore, Integer offset, Integer limit) throws ApiException {
        return getListing(null, modifiedAfter, modifiedBefore, offset, limit, Collections.emptyMap());
    }

    private ApiResponse<Tool> updateByIdApiResponse(String id, Tool data) throws ApiException {
        return updateEntity(id, data);
    }

    private ApiResponse<Tool> createToolApiResponse(Tool data) throws ApiException {
        return createNewEntity(data);
    }
}
