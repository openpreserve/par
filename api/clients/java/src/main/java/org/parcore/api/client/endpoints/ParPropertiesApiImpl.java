package org.parcore.api.client.endpoints;

import org.parcore.api.client.async.ApiCallback;
import org.parcore.api.client.utilities.AbstractApiCallImpl;
import org.parcore.api.client.utilities.ApiClient;
import org.parcore.api.client.utilities.ApiException;
import org.parcore.api.client.utilities.ApiResponse;
import org.parcore.domain.ParProperties;
import org.parcore.domain.ParProperty;

import java.util.Collections;

public class ParPropertiesApiImpl extends AbstractApiCallImpl<ParProperties, ParProperty> implements ParPropertiesApi {

    public ParPropertiesApiImpl(ApiClient apiClient) {
        super(apiClient, "/par-properties", ParProperties.class, ParProperty.class);
    }

    public ParPropertiesApiImpl(ApiClient apiClient, String[] authName) {
        this(apiClient);
        this.localVarAuthNames = authName;
    }

    public ParProperties getAllProperties() throws ApiException {
        return getListingApiResponse(null, null, null, null).getData();
    }

    public ParProperties getPagedListOfProperties(Integer offset, Integer limit) throws ApiException {
        return getListingApiResponse(null, null, offset, limit).getData();
    }

    public ParProperties getPagedListofPropertiesByModifiedDate(String modifiedAfter, String modifiedBefore, Integer offset, Integer limit) throws ApiException {
        return getListingApiResponse(modifiedAfter, modifiedBefore, offset, limit).getData();
    }

    public ParProperties getPropertiesByModifiedDate(String modifiedAfter, String modifiedBefore) throws ApiException {
        return getListingApiResponse(modifiedAfter, modifiedBefore, null, null).getData();
    }

    public void getPropertiesAsync(String modifiedAfter, String modifiedBefore, final ApiCallback<ParProperties> callback) throws ApiException {
        getListingAsync(null, modifiedAfter, modifiedBefore, Collections.emptyMap(), callback);
    }



    // --- Internal methods that call down to the AbstractClass

    private ApiResponse<ParProperties> getListingApiResponse(String modifiedAfter, String modifiedBefore, Integer offset, Integer limit) throws ApiException {
        return getListing(null, modifiedAfter, modifiedBefore, offset, limit, Collections.emptyMap());
    }

    private ApiResponse<ParProperty> getEntityApiResponse(String id) throws ApiException {
        return getEntity(id, null);
    }

    private ApiResponse<ParProperty> updateEntityApiResponse(String id, ParProperty data) throws ApiException {
        return updateEntity(id, data);
    }

    private ApiResponse<ParProperty> createEntityApiResponse(ParProperty data) throws ApiException {
        return createNewEntity(data);
    }
}
